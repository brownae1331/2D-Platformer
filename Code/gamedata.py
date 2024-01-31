# Pre-made Levels
level1 = {
    'terrain': 'Levels/1/Level1_terrain.csv',
    'crates': 'Levels/1/Level1_crates.csv',
    'fruits': 'Levels/1/Level1_fruits.csv',
    'enemies': 'Levels/1/Level1_enemies.csv',
    'checkpoints': 'Levels/1/Level1_checkpoints.csv',
    'constraints': 'Levels/1/Level1_constraints.csv',
    'obstacles': 'Levels/1/Level1_obstacles.csv'
}

level2 = {
    'terrain': 'Levels/2/Level2_terrain.csv',
    'crates': 'Levels/2/Level2_crates.csv',
    'fruits': 'Levels/2/Level2_fruits.csv',
    'enemies': 'Levels/2/Level2_enemies.csv',
    'checkpoints': 'Levels/2/Level2_checkpoints.csv',
    'constraints': 'Levels/2/Level2_constraints.csv',
    'obstacles': 'Levels/2/Level2_obstacles.csv'
}

levels = {
    0: level1,
    1: level2
}

cLevel1 = {
    'terrain': 'CustomLevels/1/Level1_terrain.csv',
    'crates': 'CustomLevels/1/Level1_crates.csv',
    'fruits': 'CustomLevels/1/Level1_fruits.csv',
    'enemies': 'CustomLevels/1/Level1_enemies.csv',
    'checkpoints': 'CustomLevels/1/Level1_checkpoints.csv',
    'constraints': 'CustomLevels/1/Level1_constraints.csv',
    'obstacles': 'CustomLevels/1/Level1_obstacles.csv'
}

customLevels = {
    0: cLevel1
}

fastestTime = {}
for i in range(30):
    exec(f'fstTime{i} = 0')
    exec(f'fastestTime{i} = fstTime{i}')
