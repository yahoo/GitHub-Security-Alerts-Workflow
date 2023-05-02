# Copyright 2019, Oath Inc.
# Licensed under the terms of the Apache 2.0 license. See LICENSE file in root for terms.

query = """{organization
              (login: "yahoo")
                 {repositories(first:100)
                   { edges
                     { node
                       {owner
                        {  id  }
                          name
                          vulnerabilityAlerts ( first: 100 )
                            {  edges
                              {  node
                                {  affectedRange
                                    dismissReason
                                    dismissedAt
                                    externalIdentifier 
                                    externalReference 
                                    fixedIn 
                                    id 
                                    packageName 
                                }
                               } 
                            } 
                        } 
                    } 
                } 
            }
        }"""
