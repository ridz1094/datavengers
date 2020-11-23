'use strict'
const AWS = require('aws-sdk');

AWS.config.update({ region: "us-east-1" });

exports.handler = async (event, context) => {
    const doc = new AWS.DynamoDB.DocumentClient({ region: "us-east-1" });

    let responseBody = ""
    let statusCode = 0;

    const { id, sender_id, receiver_id, message } = JSON.parse(event.body);

    const params = {
        TableName: "User_Messages",
        Item: {
            id: id,
            receiver_id: receiver_id,
            sender_id: sender_id,
            message: message
        }
    }

    try {
        const data = await doc.put(params).promise();
        responseBody = JSON.stringify(data);
        statusCode = 201;
        console.log(data);
    } catch (err) {
        console.log(err);
        responseBody = 'Unable to put message: ${err}';
        statusCode = 403;
    }

    const response = {
        statusCode = statusCode,
        header: {
            "Content-Type": "application/json"
        },
        body: responseBody
    };

    return response;
}