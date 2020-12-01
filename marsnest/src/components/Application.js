import React from "react";
import { useParams } from "react-router";
import './Application.css'

const Application = () => {
    return (
        <div className="container">
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
                        <form action="#" className="contact-form form-validate" noValidate="novalidate">
                            <div className="row">
                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label className="required-field" htmlFor="name">Name</label>
                                        <input type="text" className="form-control" id="name" name="name" placeholder="Name"/>
                                    </div>
                                </div>
            
                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="uniqueid">UniqueId</label>
                                        <input type="text" className="form-control" id="uniqueid" name="uniqueid" placeholder="Unique Id"/>
                                    </div>
                                </div>
            
                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label className="required-field" htmlFor="email">Email</label>
                                        <input type="text" className="form-control" id="email" name="email" placeholder="Email"/>
                                    </div>
                                </div>
            
                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="qualification">Qualification</label>
                                        <input type="text" className="form-control" id="qualification" name="qualification" placeholder="Qualification"/>
                                    </div>
                                </div>
            
                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="address">Address</label>
                                        <input type="text" className="form-control" id="address" name="address" placeholder="Address"/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="phone">Phone Number</label>
                                        <input type="text" className="form-control" id="phone" name="phone" placeholder="Phone no"/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="bgroup">Blood group</label>
                                        <input type="text" className="form-control" id="bgroup" name="bgroup" placeholder="Blood group"/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="sdate">Assignment start date</label>
                                        <input type="text" className="form-control" id="sdate" name="sdate" placeholder="Date"/>
                                    </div>
                                </div>

                                <div className="col-sm-4 mb-3">
                                    <div className="form-group">
                                        <label htmlFor="edate">Assignment end date</label>
                                        <input type="text" className="form-control" id="edate" name="edate" placeholder="Date"/>
                                    </div>
                                </div>
            
                                <div className="col-sm-12 mb-3">
                                    <div className="form-group">
                                        <label className="required-field" htmlFor="aboutme">About me</label>
                                        <textarea className="form-control" id="aboutme" name="aboutme" rows="4" placeholder="About me"></textarea>
                                    </div>
                                </div>
                                <div className="col-sm-12 mb-3">
                                    <button type="submit" name="submit" className="btn btn-primary">Submit</button>
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