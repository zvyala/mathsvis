function result = compute_cos_wave()
  x = linspace(0, 2*pi, 100);  
  y = cos(x);                  
  result = struct('x', x, 'y', y);  
end
