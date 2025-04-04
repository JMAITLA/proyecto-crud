app.delete('/tareas/:id', (req, res) => {
    const id = parseInt(req.params.id);
    tareas = tareas.filter(tarea => tarea.id !== id);
    res.send({ message: 'Tarea eliminada' });
    });