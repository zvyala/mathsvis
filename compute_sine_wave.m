function result = compute_sine_wave()
  x = linspace(0, 2*pi, 100);
  y = sin(x);
  result = struct('x', x, 'y', y);
end
