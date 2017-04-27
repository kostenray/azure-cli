# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.help_files import helps

helps['cognitiveservices list'] = """
    type: command
    short-summary: list all the existing cognitive services accounts under a resource group or current azure subscription
    examples:
        - name: list all the cognitive services accounts in a resource group 
          text: az cognitiveservices list -g MyResourceGroup
"""

#helps['cognitiveservices checkskuavailability'] = """
#    type: command
#    short-summary: check the available skus
#"""

helps['cognitiveservices account'] = """
    type: group
    short-summary: Manage and update cognitive services accounts
    
"""

helps['cognitiveservices account delete'] = """
    type: command
    short-summary: Remove a cognitive services account.
"""

helps['cognitiveservices account create'] = """
    type: command
    short-summary: Create a cognitive services account.
    examples:
        - name: create a cognitive services accounts with all required fields 
          text: az cognitiveservices create -n myresource -g myResouceGroup --Kind myAPI --Sku S0 -l WestUs
"""

helps['cognitiveservices account show'] = """
    type: command
    short-summary: Get the details of a cognitive services account.
"""

helps['cognitiveservices account update'] = """
    type: command
    short-summary: Update the properties of a cognitive services account.
"""

helps['cognitiveservices account list-skus'] = """
    type: command
    short-summary: List the avaiable skus of a cognitive services account.
"""


helps['cognitiveservices account keys'] = """
    type: group
    short-summary: Manage the keys of a cognitive services account.
"""

helps['cognitiveservices account keys regenerate'] = """
    type: command
    short-summary: Regenerate the keys of a cognitive services account.
"""

helps['cognitiveservices account keys list'] = """
    type: command
    short-summary: List the keys of a cognitive services account.
"""



