function parseUrl (queryString) {
    const res = {}
    const query = queryString.trim().replace(/^(\?|#|&)/, '')

    if (!query) {
      return res
    }
    
    query.split('&').forEach(param => {
      const parts = param.replace(/\+/g, ' ').split('=')
      const key = decodeURIComponent(parts.shift())
      const val = parts.length > 0
        ? decodeURIComponent(parts.join('='))
        : null

      if (res[key] === undefined) {
        res[key] = val
      } else if (Array.isArray(res[key])) {
        res[key].push(val)
      } else {
        res[key] = [res[key], val]
      }
    })
    return res
}

export { parseUrl }
