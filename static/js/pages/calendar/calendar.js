"use strict";
    $('#calendar').fullCalendar({
        header: {
            left: 'prev',
            center: 'title',
            right: 'next'
        },
        defaultDate: '2020-06-12',
        editable: true,
        droppable: true, // this allows things to be dropped onto the calendar
        drop: function() {
            // is the "remove after drop" checkbox checked?
            if ($('#drop-remove').is(':checked')) {
                // if so, remove the element from the "Draggable Events" list
                $(this).remove();
            }
        },
        eventLimit: true, // allow "more" link when too many events
        events: [
            {
                id: 23,
                title: 'All Day Event',
                start: '2020-06-05',
                className: 'bg-primary'
            },
            {
                title: 'Long Event',
                start: '2020-06-07',
                className: 'bg-primary'
            },
            {
                title: 'Repeating Event',
                start: '2020-06-09',
                className: 'bg-secondary'
            },
            {
                title: 'Repeating Event',
                start: '2020-06-16',
                className: 'bg-success'
            },
            {
                title: 'Conference',
                start: '2020-06-11',
                end: '2020-06-11',
                className: 'bg-danger'
            },
            {
                title: 'Meeting',
                start: '2020-06-12',
                end: '2020-06-12',
                className: 'bg-warning'
            },
            {
                title: 'Lunch',
                start: '2020-06-12',
                className: 'bg-danger'
            },
            {
                title: 'Meeting',
                start: '2020-06-12',
                className: 'b-drank'
            },
            {
                title: 'Happy Hour',
                start: '2020-06-12',
                className: 'bg-info'
            },
            {
                title: 'Dinner',
                start: '2020-06-12',
                className: 'bg-dark'
            },
            {
                title: 'Birthday Party',
                start: '2020-06-13',
                className: 'bg-dark'
            },
            {
                title: 'Click for Google',
                url: 'http://google.com/',
                start: '2020-06-28',
                className: 'bg-info'
            }
        ]
    });

    // Hide default header
    //$('.fc-header').hide();



    // Previous month action
    $('#cal-prev').on('click',function(){
        $('#calendar').fullCalendar( 'prev' );
    });

    // Next month action
    $('#cal-next').on('click',function(){
        $('#calendar').fullCalendar( 'next' );
    });

    // Change to month view
    $('#change-view-month').on('click',function(){
        $('#calendar').fullCalendar('changeView', 'month');

        // safari fix
        $('#content .main').fadeOut(0, function() {
            setTimeout( function() {
                $('#content .main').css({'display':'table'});
            }, 0);
        });

    });

    // Change to week view
    $('#change-view-week').on('click',function(){
        $('#calendar').fullCalendar( 'changeView', 'agendaWeek');

        // safari fix
        $('#content .main').fadeOut(0, function() {
            setTimeout( function() {
                $('#content .main').css({'display':'table'});
            }, 0);
        });

    });

    // Change to day view
    $('#change-view-day').on('click',function(){
        $('#calendar').fullCalendar( 'changeView','agendaDay');

        // safari fix
        $('#content .main').fadeOut(0, function() {
            setTimeout( function() {
                $('#content .main').css({'display':'table'});
            }, 0);
        });

    });

    // Change to today view
    $('#change-view-today').on('click',function(){
        $('#calendar').fullCalendar('today');
    });

    /* initialize the external events
     -----------------------------------------------------------------*/
    $('#external-events .event-control').each(function() {

        // store data so the calendar knows to render an event upon drop
        $(this).data('event', {
            title: $.trim($(this).text()), // use the element's text as the event title
            stick: true // maintain when user navigates (see docs on the renderEvent method)
        });

        // make the event draggable using jQuery UI
        $(this).draggable({
            zIndex: 999,
            revert: true,      // will cause the event to go back to its
            revertDuration: 0  //  original position after the drag
        });

    });

    $('#external-events .event-control .event-remove').on('click', function(){
        $(this).parent().remove();
    });

    // Submitting new event form
    $('#add-event').submit(function(e){
        e.preventDefault();
        var form = $(this);

        var newEvent = $('<div class="event-control p-10 mb-10">'+$('#event-title').val() +'<a class="pull-right text-muted event-remove"><i class="fa fa-trash-o"></i></a></div>');

        $('#external-events .event-control:last').after(newEvent);

        $('#external-events .event-control').each(function() {

            // store data so the calendar knows to render an event upon drop
            $(this).data('event', {
                title: $.trim($(this).text()), // use the element's text as the event title
                stick: true // maintain when user navigates (see docs on the renderEvent method)
            });

            // make the event draggable using jQuery UI
            $(this).draggable({
                zIndex: 999,
                revert: true,      // will cause the event to go back to its
                revertDuration: 0  //  original position after the drag
            });

        });

        $('#external-events .event-control .event-remove').on('click', function(){
            $(this).parent().remove();
        });

        form[0].reset();

        $('#cal-new-event').modal('hide');

    });