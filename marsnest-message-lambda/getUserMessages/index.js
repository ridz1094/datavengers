'use strict'
const AWS = require('aws-sdk');

AWS.config.update({ region: "us-east-1" });

exports.handler = async (event, context) => {
    const doc = new AWS.DynamoDB.DocumentClient({ region: "us-east-1" });

    let responseBody = ""
    let statusCode = 0;

    //console.log( event.query);
    //const { user_id } = event.query;
    const user_id = event.queryStringParameters.user_id; 

    const params = {
        TableName: "User_Messages"
    }

    try {
        const data = await doc.scan(params).promise();
        // let reduced_data = any;
        // data.Items.forEach(function(item) {
        //     console.log(" -", item.year + ": " + item.title);
        //});

        const messages = data.Items.filter(d => d.receiver_id == user_id)

        responseBody = JSON.stringify(messages);
        statusCode = 201;
        console.log(data);
    } catch (err) {
        console.log(err);
        responseBody = 'Unable to get message: ${err}';
        statusCode = 403;
    }

    // const response = {
    //     statusCode: statusCode,
    //     header: {
    //         "Content-Type": "application/json"
    //     },
    //     body: responseBody
    // };

    var response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": responseBody,
        "isBase64Encoded": false
    };

    return response;
}