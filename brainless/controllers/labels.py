"""
This is the labels module and supports all the ReST actions for LABELS
"""

from flask import abort
from configuration import db
from models.label import Label, LabelSchema

def create(user_id, account_id, label):
    """
    This function creates a new label for a specific account,
    user combination based on the passed-in label data

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param label: label to create in labels structure
    :return: 201 on success, 409 on label already exists
    """

    schema = LabelSchema()
    new_label = schema.load(label)

    if new_label.create() is None:
        abort(409, f'Label {new_label.name} already exists')
    else:
        label_serialized = schema.dump(new_label)

        return label_serialized, 201

def read(user_id, account_id, label_id):
    """
    This function retrieves a label based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param label_id: label_id passed-in URL
    :return: 200 on success, 404 on label already exists
    """

    label = Label(id=label_id,
                  name=None,
                  guid=None,
                  account_id=None,
                  brain_enabled='Y')

    read_label = label.read()

    if read_label is None:
        abort(404, f'Label with id:{label_id} not found')
    else:
        schema = LabelSchema()
        label_serialized = schema.dump(read_label)

        return label_serialized, 200

def search(user_id, account_id):
    """
    This function retrieves a list of labels based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :return: 200 on success, 404 on no labels found
    """

    existing_labels = Label.query.filter(Label.account_id == account_id).all()
    if existing_labels is None:
        abort(404, f'No labels found')

    schema = LabelSchema(many=True)
    labels_serialized = schema.dump(existing_labels)

    return labels_serialized, 200

def update(user_id, account_id, label_id, label):
    """
    This function updates label based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param label_id: label_id passed-in URL
    :param label: payload information
    :return: 200 on success, 404 on label not found
    """

    schema = LabelSchema()
    label_to_update = schema.load(label)

    updated_label = label_to_update.update()

    if updated_label is None:
        abort(404, f'Label {label_id} not found')
    else:
        label_serialized = schema.dump(updated_label)

        return label_serialized, 200

def delete(user_id, account_id, label_id):
    """
    This function deletes label based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param label_id: label_id passed-in URL
    :return: 200 on success, 404 on label not found
    """

    label_to_delete = Label(id=label_id,
                            name=None,
                            guid=None,
                            account_id=None,
                            brain_enabled='Y')

    if label_to_delete.delete() is not None:
        abort(404, f'Label {label_id} not found')
    else:
        return "Label deleted", 200
