def chain_invoke(chain, loader, url):
    return chain.invoke(
        {
            "loader_infos": loader(url),
            "input": "{input}",
        }
    ).content
