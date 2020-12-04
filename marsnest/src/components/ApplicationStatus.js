import React, {useEffect} from "react";
import { useParams } from "react-router";
import './ApplicationStatus.css'
import * as Icon from 'react-bootstrap-icons';
import { Link } from 'react-router-dom'


const ApplicationStatus = ({application}) => {

    return (

    <div className="container padding-bottom-3x mb-1">
        <div className="card mb-3">
          <div className="p-4 text-center gradient-brand-color help-box rounded-top">
            <span className="font-weight-bold">My Application</span>
          </div>
          <div className="d-flex flex-wrap flex-sm-nowrap justify-content-between py-3 px-2 bg-secondary">
            <div className="w-100 text-center py-1 px-2">
                <span className="status-title">Application no</span>
                 App#
            </div>
            <div className="w-100 text-center py-1 px-2">
                <span className="status-title">Lodged date</span>
                 Date#
            </div>
            <div className="w-100 text-center py-1 px-2">
                <span className="status-title">Status</span>
                 Stat
            </div>
          </div>
          <div className="card-body">
            <div className="steps d-flex flex-wrap flex-sm-nowrap justify-content-between padding-top-2x padding-bottom-1x">
              <div className="step completed">
                <div className="step-icon-wrap">
                  <div className="step-icon"><Icon.Person /></div>
                </div>
                <h4 className="step-title">Sign up</h4>
              </div>
              <div className={application ? 'step completed' : 'step'}>
                <div className="step-icon-wrap">
                  <div className="step-icon"><Icon.FileEarmarkText /></div>
                </div>
                <h4 className="step-title">Lodge Application</h4>
              </div>
              <div className={application ? 'step completed' : 'step'}>
                <div className="step-icon-wrap">
                  <div className="step-icon">
                    {application && application.status === 'Pending'? <Icon.Clock /> : <Icon.CheckCircle />}
                  </div>
                </div>
                <h4 className="step-title">
                    {application && application.status === 'Pending'? 'Pending' : 'Application approved'}
                </h4>
              </div>
              <div className="step">
                <div className="step-icon-wrap">
                  <div className="step-icon"><Icon.ShieldPlus/></div>
                </div>
                <h4 className="step-title">Health exam</h4>
              </div>
              <div className="step">
                <div className="step-icon-wrap">
                  <div className="step-icon"><Icon.Cursor/></div>
                </div>
                <h4 className="step-title">Ready set go!</h4>
              </div>
            </div>
          </div>
          <div className="p-4 d-flex justify-content-center ">
            <Link to='/application'>
                <button className="btn btn-primary btn-lg view-app">
                    {application ? 'View Application' : 'Lodge Application'}
                </button> 
            </Link>
          </div>
          <br/><br/>
        </div>
      </div>
    );
}



export default ApplicationStatus;