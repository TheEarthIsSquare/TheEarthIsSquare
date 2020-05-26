const path = require("path");

module.exports = {
  runtimeCompiler: true,
  configureWebpack: {
    resolve: {
      alias: {
        "@": path.resolve(__dirname, './src')
      },
      extensions: ['.js', '.vue', '.json']
    }
  },
  devServer: {
    watchOptions: {
      poll: true
    }
  }
};