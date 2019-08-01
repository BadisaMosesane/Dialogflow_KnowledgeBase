#!/usr/bin/env python

"""Dialogflow API to manage  Knowledgebase
Integrate the knowledge base to Dialogflow chatbot
"""

import argparse

#start DgFlow KB
def knowledgeBase(project_id):
        """list KB belonging to the project"""

        import dialogflow_v2beta1 as dialogflow
        client  = dialogflow.KnowledgeBasesClient()
        project_path = client.project_path(project_id)

        print('Knowledge Bases for: {}'.format(project_id) )
        for knowledge_base in client.list_knowledge_bases(project_path):
                print(' - Display Name: {}'.format(knowledge_base.display_name))
                print(' - Knowledge ID: {}\n'.format(knowledge_base.name))
#end Dgflow list KB


#create the Knowledge base
def create_knowledgeBase(project_id, display_name):
        """create Knowledge Base"""

        import dialogflow_v2beta1 as dialogflow
        client = dialogflow.KnowledgeBasesClient()
        project_path = client.project_path(project_id)

        knowledge_base = dialogflow.types.KnowledgeBase(
                display_name=display_name)

        response = client.create_knowledgeBase(project_path, knowledge_base)

        print('Knowledge Base created:\n')
        print('Display Name:{}\n'.format(response.display_name))
        print('Knowledge ID: {}\n'.format(response.name))
#end create Knowledge Base



#start get Knowledge Base
def get_knowledgeBase(project_id, knowledge_base_id):
        """gets a specific knowledge base"""
        import dialogflow_v2beta1 as dialogflow
        client = dialogflow.KnowledgeBasesClient()
        knowledge_base_path = client.knowledge_base_path(
                project_id, knowledge_base_id)

        response = client.get_knowledgeBase(knowledge_base_path)

        print('Got knowledge base:')
        print(' - Display Name: {}'.format(response.display_name)
        print(' - Knowledge ID: {}'.format(response.name))
#end get Knowledge Base

#source
#https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/dialogflow/cloud-client/knowledge_base_management.py
