from pyscript import display

band = {'Kelsey', 'Selena', 'Jennifer', 'Phoebe'}
dance = {'Jennifer', 'Jade', 'Ashley', 'Erich'}

display(f'Students in one of the clubs: {band | dance}', target='output')
display(f'Students in both clubs: {band & dance}', target='output')
display(f'Students in Band: {band - dance}', target='output')
display(f'Students in Dance: {dance - band}', target='output')

display(f'Students with only one clubs: {band ^ dance}', target='output')
