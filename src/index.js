import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App'; 


const rootElement = document.getElementById('root');

if (rootElement) {
  const root = ReactDOM.createRoot(rootElement);
  root.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>
  );
} else {
  console.error('Root element not found. Make sure your HTML file has a div with id="root".');
}