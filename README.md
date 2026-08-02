              User

               |
               v

          FastAPI

               |
               v

            Agent

               |
        ----------------

        |              |

      LLM          Tool Registry

        |              |

        |        ------------

        |        |          |

        |    Weather   Calculator

        |
        v

      Final Answer
      # Mini Agent Server


A lightweight LLM Agent backend built with FastAPI.


Features:

- Function Calling
- Tool Execution
- Multi-tool routing
- REST API
- LLM integration


Architecture:

FastAPI + LLM + Tool Registry