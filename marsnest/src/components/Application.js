import React, { useState } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import './Application.css';
import { API } from "aws-amplify";
import Loading from "./Loading";


const Application = () => {
  const {user} = useAuth0(),
  [isLoading, setIsLoading] = useState(false),
  [isSubmitted, setIsSubmitted] = useState(false),
  [uin, setUin] = useState(''),
  [qualification, setQualification] = useState(''),
  [about, setAbout] = useState(''),
  [bloodGroup, setBloodGroup] = useState(''),
  [startDate, setStartDate] = useState(''),
  [endDate, setEndDate] = useState(''),
  [address, setAddress] = useState(''),
  [userdb, setUser] = useState('');
  
  var url = "/users/email?email=" + user.email;
  API.get('application', url)
    .then(response => {
        setUser(response.data);
    })
  const submit = (e) => {
        e.preventDefault()
        setIsLoading(true);
        API.get('application', 'user_application/create',{
        queryStringParameters: {
          user_id: userdb.id,
          uin: uin,
          qualification: qualification,
          about: about,
          blood_group: bloodGroup,
          start_date: startDate,
          end_date: endDate,
          address: address
      }
      }).then(response => {
          setIsLoading(false);
          setIsSubmitted(true);
          console.log(response)
      })
    .catch(error => {
        console.log(error.response);
    });
  }

  if (isLoading) {
    return <Loading />;
  }
    return (
        <div className="container">
            <p></p>
            { isSubmitted && ( <div className="alert alert-success" role="alert">Application Submitted!</div>)}
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
                        <form  onSubmit={submit} className="contact-form form-validate">
                            <div className="row">
                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label className="required-field" htmlFor="name">Name</label>
                                        <input type="text" className="form-control" id="name" name="name" placeholder="Name" value={userdb.name} 
                                        readOnly/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label className="required-field" htmlFor="email">Email</label>
                                        <input type="text" className="form-control" id="email" name="email" placeholder="Email" value={userdb.email} 
                                        readOnly/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="phone">Phone Number</label>
                                        <input type="number" className="form-control" id="phone" name="phone" placeholder="Phone no" value={userdb.mobile} 
                                        readOnly/>
                                    </div>
                                </div>
            
                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="uniqueid">UniqueId</label>
                                        <input type="text"  className="form-control" id="uniqueid" name="uniqueid" placeholder="Unique Id" value={uin} onChange={e => { setUin(e.target.value);}}/>
                                    </div>
                                </div>
            
                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="qualification">Qualification</label>
                                        <input type="text" className="form-control" id="qualification" name="qualification" placeholder="Qualification" value={qualification} onChange={e => { setQualification(e.target.value);}}/>
                                    </div>
                                </div>
            
                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="address">Address</label>
                                        <input type="text" className="form-control" id="address" name="address" placeholder="Address" value={address} onChange={e => { setAddress(e.target.value);}}/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="bgroup">Blood group</label>
                                        <input type="text" className="form-control" id="bgroup" name="bgroup" placeholder="Blood group" value={bloodGroup} onChange={e => { setBloodGroup(e.target.value);}}/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="sdate">Assignment start date</label>
                                        <input type="text" className="form-control" id="sdate" name="sdate" placeholder="Date" value={startDate} onChange={e => { setStartDate(e.target.value);}}/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="edate">Assignment end date</label>
                                        <input type="text" className="form-control" id="edate" name="edate" placeholder="Date" value={endDate} onChange={e => { setEndDate(e.target.value);}}/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="height">Height</label>
                                        <input type="number" className="form-control" id="height" name="height" placeholder="Height"/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="weight">Weight</label>
                                        <input type="number" className="form-control" id="weight" name="weight" placeholder="Weight"/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="health">Health conditions</label>
                                        <input type="text" className="form-control" 
                                            id="health" name="health" placeholder="Health condition"/>
                                    </div>
                                </div>
            
                                <div className="col-sm-12 mb-3">
                                    <div className="form-group">
                                        <label className="required-field" htmlFor="aboutme">About me</label>
                                        <textarea className="form-control" id="aboutme" name="aboutme" rows="2" placeholder="About me" value={about} onChange={e => { setAbout(e.target.value);}}></textarea>
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