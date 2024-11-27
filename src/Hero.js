import React from 'react';
import './Hero.css';  // Import the styles for the hero section

const Hero = () => {
  return (
    <div className="hero-container">
      <div className="hero-content">
        <h1 className="hero-title">Welcome to Our Website</h1>
        <p className="hero-description">
          Discover the best services we offer and join our community today.
        </p>
        <button className="hero-btn">Get Started</button>
      </div>
    </div>
  );
};

export default Hero;
