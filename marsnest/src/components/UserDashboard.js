import React from "react";
import { useParams } from "react-router";
import Application from "./Application";
import ApplicationStatus from "./ApplicationStatus";


const UserDashboard = () => {
    let cond = true
            if(cond){
                return <Application/>
            } else {
                return <ApplicationStatus/>
            }
}



export default UserDashboard;