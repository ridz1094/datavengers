import React, { useState, useEffect } from "react";
import { useParams } from "react-router";
import './Application.css'
import { API } from "aws-amplify";
import Loading from "./Loading";

const Application = () => {

    const [isLoading, setIsLoading] = useState(true);
    const [application, setApplication] = useState();
    const [isSent, setIsSent] = useState(false)

    
    const fetchData = async () => {
        await API.get('application', 'user_applications?user_id='+ 1) // change
        .then(response => {
            if(response.data.length > 0) {
                setApplication(response.data[0]);
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

    const submit = e => {
        e.preventDefault()
        setIsLoading(true);
        try {
            API.post("application", "/user_applications", {
                body: JSON.stringify(application)
              }).then(() => {
                setIsSent(true)
                setIsLoading(false)
              })
          } catch (e) {
            setIsLoading(false);
          }
      }

      if (isLoading) {
        return <Loading />;
      }

    return (
        <div className="container">
            <p></p>
            { isSent && ( <div className="alert alert-success" role="alert">Application sent!</div>)}
            <div className="help-wrapper shadow-lg mt-n9 ">
                <div className="row no-gutters">
                    <div className="col-lg-2 help-wrapper gradient-brand-color p-5 order-lg-1 help-box">
                        <h3 className="color--white mb-5">Begin your journey!</h3>
            
                        <div>
                            Please fill in your details here!
                            <br/>
                            <br/>
                            <br/>
                            You can track the status of application here once lodged.
                        </div>
                    </div>
            
                    <div className="col-lg-10 form-wrapper p-5 order-lg-2 ">
                        <form action="#" className="contact-form form-validate" onSubmit={submit}>
                            <div className="row">
                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label className="required-field" htmlFor="name">Name</label>
                                        <input type="text" 
                                            className="form-control" 
                                            id="name" name="name" placeholder="Name"
                                             />
                                    </div>
                                </div>
            
                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="uniqueid">UniqueId</label>
                                        <input type="text" 
                                            className="form-control" 
                                            id="uniqueid" name="uniqueid" placeholder="Unique Id"
                                            value={application.uniqueId}
                                            onChange={e => setApplication({ ...application, uniqueId: e.target.value })}/>
                                    </div>
                                </div>
            
                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label className="required-field" htmlFor="email">Email</label>
                                        <input type="text" className="form-control" 
                                            id="email" name="email" placeholder="Email"/>
                                    </div>
                                </div>
            
                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="qualification">Qualification</label>
                                        <input type="text" className="form-control" 
                                            id="qualification" name="qualification" placeholder="Qualification"
                                            value={application.qualification}
                                            onChange={e => setApplication({ ...application, qualification: e.target.value })}/>
                                    </div>
                                </div>
            
                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="address">Address</label>
                                        <input type="text" className="form-control" id="address"
                                            name="address" placeholder="Address"
                                            value={application.address_text}
                                            onChange={e => setApplication({ ...application, address_text: e.target.value })}/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="phone">Phone Number</label>
                                        <input type="text" className="form-control" 
                                            id="phone" name="phone" placeholder="Phone no" />
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="bgroup">Blood group</label>
                                        <input type="text" className="form-control" 
                                            id="bgroup" name="bgroup" placeholder="Blood group" 
                                            value={application.blood_group}
                                            onChange={e => setApplication({ ...application, blood_group: e.target.value })}/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="sdate">Assignment start date</label>
                                        <input type="text" className="form-control"
                                             id="sdate" name="sdate" placeholder="Date" 
                                             value={application.start_date}
                                             onChange={e => setApplication({ ...application, start_date: e.target.value })}/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="edate">Assignment end date</label>
                                        <input type="text" className="form-control"
                                             id="edate" name="edate" placeholder="Date"
                                             value={application.end_date}
                                             onChange={e => setApplication({ ...application, end_date: e.target.value })}/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="height">Height</label>
                                        <input type="text" 
                                            className="form-control" id="height" name="height" 
                                            value={application.height}
                                            placeholder="Height" 
                                            onChange={e => setApplication({ ...application, height: e.target.value })}/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="weight">Weight</label>
                                        <input type="text" className="form-control"
                                            id="weight" name="weight" placeholder="Weight"
                                            value={application.weight}
                                            onChange={e => setApplication({ ...application, weight: e.target.value })}/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="health">Health conditions</label>
                                        <input type="text" className="form-control" 
                                            id="health" name="health" placeholder="Health condition"
                                            value={application.diseases}
                                            onChange={e => setApplication({ ...application, diseases: e.target.value })}/>
                                    </div>
                                </div>
            
                                <div className="col-sm-12 mb-3">
                                    <div className="form-group">
                                        <label className="required-field" htmlFor="aboutme">About me</label>
                                        <textarea className="form-control" 
                                            id="aboutme" name="aboutme" rows="2" placeholder="About me"
                                            value={application.about}
                                            onChange={e => setApplication({ ...application, about: e.target.value })}/>
                                    </div>
                                </div>
                                <div className="col-sm-12 mb-3">
                                    <button type="submit" name="submit" className="btn btn-primary btn-lg view-app">Submit</button>
                                </div>
            
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>

    );
}



export default Application;