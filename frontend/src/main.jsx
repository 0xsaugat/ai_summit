import React from 'react';
import { createRoot } from 'react-dom/client';
import LightRays from './LightRays';

const mountNode = document.getElementById('hero-react-root');

if (mountNode) {
  const root = createRoot(mountNode);

  root.render(
    <div style={{ width: '100%', height: '600px', position: 'relative' }}>
      <LightRays
        raysOrigin="top-center"
        raysColor="#ffffff"
        raysSpeed={1}
        lightSpread={0.5}
        rayLength={3}
        followMouse={true}
        mouseInfluence={0.1}
        noiseAmount={0}
        distortion={0}
        className="custom-rays"
        pulsating={false}
        fadeDistance={1}
        saturation={1}
      />
    </div>
  );
}
