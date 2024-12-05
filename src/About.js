import React from 'react';
import './About.css';
import {  Link } from 'react-router-dom';
import { Navbar, Nav } from 'react-bootstrap'; // Import Bootstrap components
const About = () => {
  return (
    
      <Navbar bg="light" expand="lg">
        <Navbar.Toggle aria-controls="navbar-nav" />
        <Navbar.Collapse id="navbar-nav">
          <Nav className="ml-auto">
            <Nav.Link as={Link} to="/aboutus">About Us</Nav.Link>
            <Nav.Link as={Link} to="/empower">Empowering Girls</Nav.Link>
            <Nav.Link as={Link} to="/programs">Programs</Nav.Link>
            <Nav.Link as={Link} to="/news">News</Nav.Link>
            <Nav.Link as={Link} to="/landing">Landing</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    
  );
};

export default About;
