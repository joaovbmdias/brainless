"""
This is the labels module and supports all the ReST actions for LABELS
"""

from flask import abort
from configuration import db
from models.label import Label, LabelSchema
from sqlalchemy.orm.exc import NoResultFound

def create(user_id, account_id, label):
    """
    This function creates a new label for a specific account,
    user combination based on the passed-in label data

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param label: label to create in labels structure
    :return: 201 on success, 409 on label already exists
    """

    # get provided label guid
    guid = label.get('guid')

    # validate if a label with the provided data exists
    existing_label = (Label.query.filter(Label.account_id == account_id)
                                 .filter(Label.guid == guid)
                                 .one_or_none())

    if existing_label is None:

        schema = LabelSchema()

        # Create a label instance using the schema and the passed-in label
        new_label = schema.load(label)

        # Add the label to the database
        db.session.add(new_label)

        db.session.commit()

        # return the newly created label id in the response
        return new_label.label_id , 201

    else:
        abort(409, f'Label {guid} already exists for account {account_id}')

def read(user_id, account_id, label_id):
    """
    This function retrieves a label based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param label_id: label_id passed-in URL
    :return: 200 on success, 404 on label already exists
    """

    try:
        # get label if it exists
        existing_label = Label.query.filter(Label.label_id == label_id).one()
    except NoResultFound:
        abort(404, f'Label with id:{label_id} not found')

    schema = LabelSchema()
    label = schema.dump(existing_label)

    return label, 200

def search(user_id, account_id):
    """
    This function retrieves a list of labels based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :return: 200 on success, 404 on no labels found
    """

    # search labels for the user and acount ids provided
    existing_labels = Label.query.filter(Label.account_id == account_id).all()
    if existing_labels is None:
        abort(404, f'No labels found')

    schema = LabelSchema(many=True)
    labels = schema.dump(existing_labels)

    return labels, 200

def update(user_id, account_id, label_id, label):
    """
    This function updates label based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param label_id: label_id passed-in URL
    :param label: payload information
    :return: 200 on success, 404 on label not found
    """

    try:
        # validate if label exists
        existing_label = Label.query.filter(Label.label_id == label_id).one()    
    except NoResultFound:
        abort(404, f'Label {label_id} not found')
    
    schema = LabelSchema()

    # Create an label instance using the schema and the passed-in label
    updated_label = schema.load(label)

    # Set the id to the label we want to update
    updated_label.label_id = existing_label.label_id

    # Add the label to the database
    db.session.merge(updated_label)
    db.session.commit()

    return "Label updated", 200

def delete(user_id, account_id, label_id):
    """
    This function deletes label based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param label_id: label_id passed-in URL
    :return: 200 on success, 404 on label not found
    """

    try:
        # validate if label exists
        existing_label = Label.query.filter(Label.label_id == label_id).one()
    except NoResultFound:
        abort(404, f'Label {label_id} not found')

    # Add the label to the database
    db.session.delete(existing_label)
    db.session.commit()

    return "Label deleted", 200
