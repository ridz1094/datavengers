import React from "react";
import { useParams } from "react-router";
import './ApplicationStatus.css'
import * as Icon from 'react-bootstrap-icons';


const ApplicationStatus = ({application}) => {
    return (

    <div class="container padding-bottom-3x mb-1">
        <div class="card mb-3">
          <div class="p-4 text-center gradient-brand-color help-box rounded-top">
            <span class="font-weight-bold">My Application</span>
          </div>
          <div class="d-flex flex-wrap flex-sm-nowrap justify-content-between py-3 px-2 bg-secondary">
            <div class="w-100 text-center py-1 px-2"><span class="status-title">Application no</span> App#</div>
            <div class="w-100 text-center py-1 px-2"><span class="status-title">Lodged date</span> Date#</div>
            <div class="w-100 text-center py-1 px-2"><span class="status-title">Status</span> Stat</div>
          </div>
          <div class="card-body">
            <div class="steps d-flex flex-wrap flex-sm-nowrap justify-content-between padding-top-2x padding-bottom-1x">
              <div class="step completed">
                <div class="step-icon-wrap">
                  <div class="step-icon"><Icon.Person /></div>
                </div>
                <h4 class="step-title">Sign up</h4>
              </div>
              <div class="step completed">
                <div class="step-icon-wrap">
                  <div class="step-icon"><Icon.FileEarmarkText /></div>
                </div>
                <h4 class="step-title">Lodge Application</h4>
              </div>
              <div class="step completed">
                <div class="step-icon-wrap">
                  <div class="step-icon"><Icon.Clock /></div>
                </div>
                <h4 class="step-title">Pending</h4>
              </div>
              <div class="step completed">
                <div class="step-icon-wrap">
                  <div class="step-icon"><Icon.CheckCircle/></div>
                </div>
                <h4 class="step-title">Application approval</h4>
              </div>
              <div class="step">
                <div class="step-icon-wrap">
                  <div class="step-icon"><Icon.ShieldFillPlus/></div>
                </div>
                <h4 class="step-title">Health exam</h4>
              </div>
              <div class="step">
                <div class="step-icon-wrap">
                  <div class="step-icon"><Icon.CursorFill/></div>
                </div>
                <h4 class="step-title">Ready set go!</h4>
              </div>
            </div>
          </div>
          <div class="p-4 d-flex justify-content-center ">
            <button class="btn btn-primary btn-lg view-app">View Application</button> 
          </div>
          <br/><br/>
        </div>
      </div>
    );
}



export default ApplicationStatus;