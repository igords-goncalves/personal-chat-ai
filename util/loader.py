"""_summary_

  Essa função vai reutilizada para carregar diversos
  loaders sem repetição de código.
"""

def loader(doc_loader):
    loader = doc_loader
    document = loader.load()

    info = ""
    for info in document:
        info += info.page_content

    return info