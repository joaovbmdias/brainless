"""
This is the labels module and supports all the ReST actions for LABELS
"""

from flask import abort
from configuration import db
from models.label import Label, LabelSchema
from constants import FAILURE

def create(user_id, account_id, body):
    """
    This function creates a new label for a specific account,
    user combination based on the passed-in label data

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param body: label to create in labels structure
    :return: 201 on success, 409 on label already exists
    """
    schema = LabelSchema()
    label = schema.load(body)
    if label.create() == FAILURE:
        abort(409, f'Label {label.name} already exists')
    else:
        return schema.dump(label), 201

def read(user_id, account_id, label_id):
    """
    This function retrieves a label based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param label_id: label_id passed-in URL
    :return: 200 on success, 404 on label already exists
    """
    label = Label(id            = label_id,
                  name          = None,
                  order         = None,
                  guid          = None,
                  account_id    = None,
                  brain_enabled = 'Y')
    if label.read() == FAILURE:
        abort(404, f'Label with id:{label_id} not found')
    else:
        schema = LabelSchema()
        return schema.dump(label), 200

def search(user_id, account_id):
    """
    This function retrieves a list of labels based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :return: 200 on success, 404 on no labels found
    """
    labels = Label.query.filter(Label.account_id == account_id).all()
    if labels is None:
        abort(404, f'No labels found')
    schema = LabelSchema(many=True)
    return schema.dump(labels), 200

def update(user_id, account_id, label_id, body):
    """
    This function updates label based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param label_id: label_id passed-in URL
    :param body: payload information
    :return: 200 on success, 404 on label not found
    """
    schema = LabelSchema()
    label = schema.load(body)
    if label.update() == FAILURE:
        abort(404, f'Label {label_id} not found')
    else:
        return schema.dump(label), 200

def delete(user_id, account_id, label_id):
    """
    This function deletes label based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param label_id: label_id passed-in URL
    :return: 200 on success, 404 on label not found
    """
    labels = Label(id            =label_id,
                   name          = None,
                   order         = None,
                   guid          = None,
                   account_id    = None,
                   brain_enabled = 'Y')
    if labels.delete() == FAILURE:
        abort(404, f'Label {label_id} not found')
    else:
        return "Label deleted", 200
