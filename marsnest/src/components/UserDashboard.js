import React, {useEffect, useState} from "react";
import Application from "./Application";
import ApplicationStatus from "./ApplicationStatus";
import { API } from "aws-amplify";
import Loading from "./Loading";
import { useAuth0 } from "@auth0/auth0-react";


const UserDashboard = () => {
  const { user } = useAuth0();
  const [isLoading, setIsLoading] = useState(true);
  const [application, setApplication] = useState();
  
  const fetchData = async () => {
    await API.get('application', 'user_applications?user_id'+ user.id)
      .then(response => {
        setApplication(response.data[0]);
        console.log(response.data[0]);
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

  if(application.status === 'Pending'){
    return <ApplicationStatus application={application}/>
  } else {
    return <Application/>
  }
}

export default UserDashboard;