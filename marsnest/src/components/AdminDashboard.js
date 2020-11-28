import React, { useState, useEffect } from "react";

import { useAuth0 } from "@auth0/auth0-react";
import { API } from "aws-amplify";
import "./AdminDashboard.css";
import Loading from "./Loading";
import { Modal} from "reactstrap";

const AdminDashboard = () => {
  
    const [applications, setApplications] = useState([]);
    const [isLoading, setLoading] = useState(true);
    const [currentApplication, setCurrentApplication] = useState({});

    const fetchData = async () => {
        API.get('application', 'user_applications')
        .then(response => {
            setApplications(response.data);
            setLoading(false);
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

    return (
        applications.map(application => (
            <div className="container" key={application.id}>
                <div className="col-md-12">
                    <div className="card b-1 hover-shadow mb-20">
                        <div className="media card-body">
                            <div className="media-left pr-12">
                                <img className="avatar avatar-xl no-radius" 
                                    src={require('../assets/avatar_male.png')}  alt="..."/>
                            </div>
                            <div className="media-body">
                                <div className="mb-2">
                                    <span className="fs-20 pr-16">Jon Doe</span>
                                </div>
                                <small className="fs-16 fw-300 ls-1">{application.qualification}</small>
                            </div>
                            <div className="media-right text-right d-none d-md-block">
                                <p className="fs-14 text-fade mb-12">
                                    <i className="fa fa-map-marker pr-1"></i> {application.status}</p>
                            </div>
                        </div>
                        <footer className="card-footer flexbox align-items-center">
                            <div>
                                <strong>Applied on:</strong>
                                <span>{application.created_at}</span>
                            </div>
                            <div className="card-hover-show">
                                <button 
                                    className="btn btn-xs fs-10 btn-bold btn-info" 
                                    onClick={() => {setCurrentApplication(application)}}>
                                    View Details</button>
                                <button className="btn btn-xs fs-10 btn-bold btn-primary">Approve</button>
                                <button className="btn btn-xs fs-10 btn-bold btn-warning" >Reject</button>
                            </div>
                        </footer>
                    </div>
                </div>
            </div>
        )
      )
    )
};

export default AdminDashboard;
