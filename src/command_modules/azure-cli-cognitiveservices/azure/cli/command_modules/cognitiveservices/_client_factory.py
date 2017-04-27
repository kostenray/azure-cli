# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

def cognitiveservices_client_factory(_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient
<<<<<<< HEAD
    return get_mgmt_service_client(CognitiveServicesManagementClient, location='notused').cognitive_services_accounts

def cognitiveservices_account_client_factory(_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient
    return get_mgmt_service_client(CognitiveServicesManagementClient, location='notused').accounts
=======
    return get_mgmt_service_client(CognitiveServicesManagementClient).cognitive_services_accounts


>>>>>>> 2161b0d84b9e572fb106610331fd68417c962f8d
