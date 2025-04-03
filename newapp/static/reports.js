document.addEventListener('DOMContentLoaded', function() {
    const reportSections = document.querySelectorAll('.report-section');

    reportSections.forEach(section => {
        const generateButton = section.querySelector('.generate-button');
        const reportPlaceholder = section.querySelector('.report-placeholder');
        const reportTitle = section.querySelector('h2').textContent;

        generateButton.addEventListener('click', function() {
            reportPlaceholder.textContent = 'Generating report...';

            // Simulate fetching data (replace with your actual data fetching logic)
            setTimeout(() => {
                let reportData = '';
                if (reportTitle.includes('Student List')) {
                    reportData = "List of all students:\n- Student A\n- Student B\n- Student C\n...";
                } else if (reportTitle.includes('Course Enrollment')) {
                    reportData = "Course Enrollment:\n- Math: 30 students\n- Science: 45 students\n- History: 25 students\n...";
                } else if (reportTitle.includes('Attendance Summary')) {
                    reportData = "Attendance Summary:\n- Average attendance: 85%\n- Students with perfect attendance: 10\n- Students with low attendance: 5\n...";
                } else {
                    reportData = 'Report data not available.';
                }
                reportPlaceholder.textContent = reportData;
            }, 1500); // Simulate a 1.5-second loading time
        });
    });
});