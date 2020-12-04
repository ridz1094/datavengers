import React, {useEffect, useState} from "react";
import Application from "./Application";
import ApplicationStatus from "./ApplicationStatus";
import { API } from "aws-amplify";
import Loading from "./Loading";
import { useAuth0 } from "@auth0/auth0-react";
import history from "../utils/history";


const UserDashboard = () => {
  const { user } = useAuth0();
  const [isLoading, setIsLoading] = useState(true);
  const [application, setApplication] = useState();
  // const {user} = history.location.state;
  
  const fetchData = async () => {
    await API.get('application', 'user/user_applications?email='+ user.email)
      .then(response => {
        if(response.data.length > 0) {
            setApplication(response.data[0]);
            // console.log(user)
        }
        setIsLoading(false);
      })
      .catch(error => {
        console.log(error.response);
    });
  }


  useEffect(() => {
    fetchData();
  }, []);

  if (isLoading) {
    return <Loading />;
  }

  return <ApplicationStatus application={application}/>
}

export default UserDashboard;