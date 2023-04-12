import React, { useEffect, useRef } from "react";
import "../styles/businesssection.css";
import business from "../images/business.png";

function BusinessSection() {
  const imageRef = useRef(null);

  useEffect(() => {
    const handleScroll = () => {
      const image = imageRef.current;
      const imagePosition = image.getBoundingClientRect().top;
      const screenPosition = window.innerHeight / 2;
      
      if (imagePosition < screenPosition) {
        image.classList.add('visible');
      } else {
        image.classList.remove('visible');
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => {
      window.removeEventListener('scroll', handleScroll);
    }
  }, []);

  return (
    <div className="business-container">
      <div className="business-text">
        <h2 className="business-title">Business</h2>
        <p className="business-description">
          Take your business to new heights with <br />
          SikePay's business account. By partnering with us,
          you'll gain limitless access to our comprehensive suite of services 
          designed to support your growth. Whether you need easy payment solutions, flexible banking options, 
          or access to business loans, we've got you covered. Plus, our wider 
          acceptance means you can do business with even more customers and suppliers. 
          Join us today 
          and start realizing your business's full potential!
        </p>
      </div>
      <div className="business-image">
        <img src={business} alt="Business" ref={imageRef} />
      </div>
    </div>
  );
}

export default BusinessSection;


