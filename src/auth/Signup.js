import React, { useState } from 'react';
import { Button, Form } from 'react-bootstrap';  // Bootstrap components
// import './Sugnup.css';  // Import custom CSS for additional styling

const SignUp = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic here (e.g., API call)
    console.log('Name:', name);
    console.log('Email:', email);
    console.log('Password:', password);
  };

  return (
    <div className="signup-container d-flex justify-content-center align-items-center">
      <div className="signup-form p-4">
        <h2 className="text-center mb-4">Sign Up</h2>
        <Form onSubmit={handleSubmit}>
          <Form.Group controlId="formName">
            <Form.Label>Name</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter your name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
            />
          </Form.Group>

          <Form.Group controlId="formEmail" className="mt-3">
            <Form.Label>Email address</Form.Label>
            <Form.Control
              type="email"
              placeholder="Enter your email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </Form.Group>

          <Form.Group controlId="formPassword" className="mt-3">
            <Form.Label>Password</Form.Label>
            <Form.Control
              type="password"
              placeholder="Enter your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </Form.Group>

          <Button variant="primary" type="submit" className="mt-4 w-100">
            Sign Up
          </Button>
        </Form>
      </div>
    </div>
  );
};

export default SignUp;
