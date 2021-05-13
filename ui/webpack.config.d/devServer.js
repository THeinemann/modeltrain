
(() => {

    const paths = ['/sections', '/switches', '/direction', '/speed']
    const host = 'http://localhost:8080'
    const port = 8008

    if (config.devServer) {

        const proxy = {}
        for (path of paths) {
            proxy[path] = host
        }
        config.devServer = { ...config.devServer, proxy, port  }
    }
})()
