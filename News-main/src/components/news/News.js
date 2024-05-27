import React, { useState, useEffect } from 'react';
import axios from 'axios';
import "./News.css";
function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      const defaultUrl = "https://www.akc.org/expert-advice/health/intestinal-blockage-in-dogs/";
      try {
        const response = await axios.get(`http://localhost:5000/extract-text/${encodeURIComponent(defaultUrl)}`);
        if (response.status !== 200) {
          throw new Error('Failed to extract text from URL.');
        }
        setData(response.data);
        setError('');
      } catch (error) {
        setError('Failed to extract text from URL.');
        setData(null);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h2>Actualités :</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {data && (
        <div className="card-b">
          <div className="card-body">
            
            {data.titles.map((title, index) => (
              <div className='card' key={index}>
                <h3>{title}</h3>
                {data.paragraphs[index] && <p>{data.paragraphs[index]}</p>}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
