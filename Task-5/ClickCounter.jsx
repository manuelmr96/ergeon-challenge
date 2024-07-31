import React, { useState } from 'react';

const ClickCounter = ({ initialCount = 0 }) => {
  const [count, setCount] = useState(initialCount);

  const handleClick = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <button onClick={handleClick}>Click count: {count}</button>
    </div>
  );
};

export default ClickCounter;