from langchain_community.document_loaders import WebBaseLoader

"""_summary_
  Basicamente estamos fazendo com que o bot responda as coisas
  baseado nas informações de determinado site.
  
  @https://python.langchain.com/api_reference/community/document_loaders.html
  @https://hub.asimov.academy/tutorial/document-loaders-no-langchain-o-que-sao-e-como-utilizar/
  
  Estamos fazendo um webscraping do site.
"""


def web_loader(url: str):
    loader = WebBaseLoader(web_path=url)
    document_list = loader.load()
    # print(document_list[0].page_content) --> debuug

    web_info = ""
    for info in document_list:
        web_info += info.page_content

    return web_info
    
