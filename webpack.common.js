const webpack = require('webpack');
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

// To work with the bundle
// on host machine install nodejs 'choco install nodejs' if you have chocolatey installed
// Then in the terminal in the project run 'npm install' the first time
// to develop run 'npm run dev'
// to save changes and build the bundle run 'npm run bundle'
// to import the bundle's code into your template include:
// <script src="{% static 'scripts/filename-bundle.js'  %}"></script>

module.exports = {
    entry: {
        customer: './js_assets/page_components/customer_view.tsx',
        employee: './js_assets/page_components/employee_view.tsx',
        order_form: './js_assets/page_components/order_form.js',
        index: './js_assets/page_components/index_scripts.js',
    },
    plugins: [
        new HtmlWebpackPlugin({
            title: 'Production',
        }),
        new webpack.ContextReplacementPlugin(/moment[/\\]locale$/, /en/),
    ],
    module: {
        rules: [{
            // Include ts, tsx, js, and jsx files.
            test: /\.(ts|js)x?$/,
            exclude: /node_modules/,
            loader: 'babel-loader',
        }],
    },
    resolve: {
        extensions: ['.ts', '.tsx', '.js', '.json']
    },
    output: {
        filename: '[name]-bundle.js',  // output bundle file name
        path: path.resolve(__dirname, './base/static/scripts'),  // path to our Django static directory
        clean: true,
    },
};
