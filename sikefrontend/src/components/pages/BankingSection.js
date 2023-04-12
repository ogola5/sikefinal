import React, { useEffect, useRef } from "react";
import "../styles/bankingsection.css";
import banking from "../images/banking.png";

function BankingSection() {
  const bankingRef = useRef(null);

  useEffect(() => {
    const handleScroll = () => {
      const bankingTop = bankingRef.current.offsetTop;
      const bankingHeight = bankingRef.current.offsetHeight;
      const windowHeight = window.innerHeight;
      const scrollTop = window.pageYOffset;
      const scrollBottom = scrollTop + windowHeight;

      if (scrollBottom > bankingTop + bankingHeight / 2 && scrollTop < bankingTop + bankingHeight) {
        bankingRef.current.classList.add("show");
      }
    };

    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <div className="banking-container" ref={bankingRef}>
      <div className="banking-text">
        <h2 className="banking-title">Banking</h2>
        <p>
          Unlock your business's potential with SikePay's comprehensive banking solutions.
          <br />
          With attractive interest rates for savings and flexible loan options tailored to your needs,
          <br />
          we're here to help fuel your growth and achieve your financial goals.
          <br />
          Partner with us and take your business to the next level!
        </p>
      </div>
      <div className="banking-image">
        <img src={banking} alt="Banking" />
      </div>
    </div>
  );
}

export default BankingSection;


