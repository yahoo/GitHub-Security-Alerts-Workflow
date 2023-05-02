#Copyright 2019, Oath Inc.
#Licensed under the terms of the Apache 2.0 license. See LICENSE file in root for terms.


#Commenting for now as the new query is used in graph_ql.py file

# query = """{organization
#               (login: "yahoo")
#                  {repositories(first:100)
#                    { edges
#                      { node
#                        {owner
#                         {  id  }
#                           name
#                           vulnerabilityAlerts ( first: 100 )
#                             {  edges
#                               {  node
#                                 {  affectedRange
#                                     dismissReason
#                                     dismissedAt
#                                     externalIdentifier
#                                     externalReference
#                                     fixedIn
#                                     id
#                                     packageName
#                                 }
#                                }
#                             }
#                         }
#                     }
#                 }
#             }
#         }"""
