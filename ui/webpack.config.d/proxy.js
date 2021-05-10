
(() => {

    const paths = ['/sections', '/switches', '/direction']
    const host = 'http://pi:5000'

    if (config.devServer) {
        const proxy = {}
        for (path of paths) {
            proxy[path] = host
        }
        config.devServer.proxy = proxy
    }
})()
