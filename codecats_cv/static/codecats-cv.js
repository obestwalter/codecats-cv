$(document)
    .ready(function () {
        $('.attached.progress.demo')
            .progress({
                label: false,
                value: Math.floor(Math.random() * 5) + 1
            })
        ;
        $('.basic.progress.demo')
            .progress({
                label: false,
                value: Math.floor(Math.random() * 5) + 1,
                text: {
                    active: '{percent}% Complete',
                    success: 'Done!'
                }
            })
        ;
        $('.indicating.progress.demo')
            .progress({
                label: true,
                total: 10,
                value: Math.floor(Math.random() * 5) + 1,
                text: {
                    active: '{percent}% Done',
                    success: 'Completed!'
                }
            })
        ;
        $('.file.progress.demo')
            .progress({
                label: false,
                text: {
                    active: 'Uploading {value} of {total}',
                    success: '{total} Files Uploaded!'
                }
            })
        ;
        var progress = function () {
            $('.demo.progress').progress('increment');
            setTimeout(progress, (Math.random() * 2000) + 300);
        };
        setTimeout(progress, 1000);

        setInterval(function () {
            $('.demo.progress').progress('reset');
        }, 30000);
    });
