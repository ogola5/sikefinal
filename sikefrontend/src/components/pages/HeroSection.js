import React, { useEffect } from "react";
import "../styles/hero.css";
import hero from "../images/hero.png";

function HeroSection() {
  useEffect(() => {
    const text = document.querySelector(".hero-text h1");
    const image = document.querySelector(".hero-image img");
    text.classList.add("fade-in");
    setTimeout(() => {
      text.classList.remove("fade-in");
      text.classList.add("fade-out");
      image.classList.add("slide-in");
    }, 4000);
  }, []);

  return (
    <div className="hero-container">
      <div className="hero-image">
        <img src={hero} alt="Hero" />
      </div>
      <div className="hero-text">
        <h1>
          <span>Welcome to </span>Sikepay
        </h1>
        <p>
          Unlock the potential of your business with our comprehensive banking
          and payment solutions.
        </p>
        <button>Get Started</button>
      </div>
    </div>
  );
}

export default HeroSection;


