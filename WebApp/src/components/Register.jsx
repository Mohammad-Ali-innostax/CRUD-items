import React, { useState } from "react";
import axios from "axios";

function Register(props){
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [displayWrongNone, setDisplayWrongNone] = useState("None");
    const [displayRightNone, setDisplayRightNone] = useState("None");

    const handleSubmit = (event) => {
        event.preventDefault();
        registerUser(username,password);
    }

    function registerUser(username, password){
        var payload = [{
            "username":username,
            "password": password
        }];
        axios.post(`http://127.0.0.1:9000/register/`, payload)
        .then(function (response){
            if(response.data === "200"){
                setDisplayRightNone("block");
                setDisplayWrongNone("None");
            }else{
                setDisplayWrongNone("block");
                setDisplayRightNone("None");
                setUsername("");
                setPassword("");
            }
        }).catch( function (error){
            console.log(error);
        });
    }

    function changeToRegister(){
        props.setChangeToRegister(false);
    }

    return(
    <div className="login-body register-body">
        <form onSubmit={handleSubmit}>
            <input type="text" value={username} placeholder="Enter Username" onChange={(e) => setUsername(e.target.value)} required/>
            <input type="password" value={password} placeholder="Enter Password" onChange={(e) => setPassword(e.target.value)} required/>
            <div className="wrong-login" style={{display: displayWrongNone}}>Please try again.</div>
            <div className="registration-done" style={{display: displayRightNone}}>Registration Done.</div>
            <button type="submit">Register</button>

            <button className="extra-button" onClick={changeToRegister}>Login Window</button>
        </form>
    </div>
);
}

export default Register;