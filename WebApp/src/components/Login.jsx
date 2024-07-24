import React, { useState } from "react";

function Login(props){
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [displayNone, setDisplayNone] = useState("None");

    const user = "Qwerty";
    const pass = "1234";

    const handleSubmit = (event) => {
        event.preventDefault();
        // console.log(username, password);
        validateLogin(username,password);
    }

    function validateLogin(username,password){
        if(username === user && password === pass){
            props.setIsAuthenticated(true);
        }else{
            props.setIsAuthenticated(false);
            setDisplayNone("block");
            setUsername("");
            setPassword("");
        }
    }

    return(
    <div className="login-body">
        <form onSubmit={handleSubmit}>
            <input type="text" value={username} placeholder="Enter Username" onChange={(e) => setUsername(e.target.value)} />
            <input type="password" value={password} placeholder="Enter Password" onChange={(e) => setPassword(e.target.value)} />
           
            <button type="submit">Login</button>
        <div className="wrong-login" style={{display: displayNone}}>Incorrect Username or Password. Try again.</div>
        </form>
    </div>
);
}

export default Login;