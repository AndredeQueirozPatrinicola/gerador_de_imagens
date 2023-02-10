const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry: {
        app: './frontend/src/index.js'
    },
    watch: true,
    devtool: 'source-map',
    output:{
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'frontend/build/static/js')
    },
    plugins: [new MiniCssExtractPlugin()],
    module : {
        rules : [
            {
                test:/\.js$/,
                exclude: /node_modules/,
            },
            {
                test: /\.css$/i,
                use: [MiniCssExtractPlugin.loader, "css-loader"],
            },
        ]
    },
    resolve:{
        extensions: [
            '.js'
        ]
    }
}