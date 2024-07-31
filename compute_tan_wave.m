function result = compute_tan_wave()
  x = linspace(0, 2*pi, 100); 
  y = tan(x);                  
  
  y = where(abs(y) > 10, NaN, y);  

  result = struct('x', x, 'y', y);  
end
