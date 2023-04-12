import React, { useRef, useEffect } from "react";
import "../styles/paymentsection.css"; // import your CSS file
import payment from "../images/payment.png"; // import your payments image

function PaymentsSection() {
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
    <div className="payments-container">
      <h2 className="section-title">Payments</h2>
      <div className="payments-content">
        <div className="payments-description">
          <p>Grow your business and streamline payments with SikePay's integrated payment systems. Offer your customers the convenience and security of major payment options such as credit and debit cards, online transfers, and more. Our reliable and user-friendly payment solutions are designed to support your business and enhance your customer's experience. Sign up now and start maximizing your potential!</p>
        </div>
        <div className="payments-image-container">
          <img src={payment} alt="Payments" ref={imageRef} />
        </div>
      </div>
    </div>
  );
}

export default PaymentsSection;






