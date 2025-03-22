// Add Skill
document.getElementById('add-skill').addEventListener('click', function () {
  const skillsSection = document.getElementById('skills-section');
  const newSkillInput = document.createElement('input');
  newSkillInput.type = 'text';
  newSkillInput.name = 'skill_name';
  newSkillInput.placeholder = 'Skill Name';
  skillsSection.appendChild(newSkillInput);
});

// Add Education
document.getElementById('add-education').addEventListener('click', function () {
  const educationSection = document.getElementById('education-section');
  const newEducationInput = document.createElement('input');
  newEducationInput.type = 'text';
  newEducationInput.name = 'institute';
  newEducationInput.placeholder = 'Institute';
  educationSection.appendChild(newEducationInput);
});

// Add Experience
document.getElementById('add-experience').addEventListener('click', function () {
  const experienceSection = document.getElementById('experience-section');
  const newExperienceInput = document.createElement('input');
  newExperienceInput.type = 'text';
  newExperienceInput.name = 'company_name';
  newExperienceInput.placeholder = 'Company Name';
  experienceSection.appendChild(newExperienceInput);
});

// Add Project
document.getElementById('add-project').addEventListener('click', function () {
  const projectsSection = document.getElementById('projects-section');
  const newProjectInput = document.createElement('input');
  newProjectInput.type = 'text';
  newProjectInput.name = 'project_title';
  newProjectInput.placeholder = 'Project Title';
  projectsSection.appendChild(newProjectInput);
});