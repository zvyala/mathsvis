function result = compute_sine_wave()
  % Example: Generate sine wave data
  x = linspace(0, 2*pi, 100);
  y = sin(x);
  result = struct('x', x, 'y', y);
end
