import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ProductList() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/onlinestore/Products/')
      .then(response => {
        setProducts(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h1>Products</h1>
      {products.map(product => (
        <div key={product.id}>
          <h2>{product.name}</h2>
          <p>{product.price}</p>
          <p>{product.digital ? 'Digital' : 'Physical'}</p>
          <img src={product.image} alt={product.name} />
        </div>
      ))}
    </div>
  );
}

export default ProductList;
