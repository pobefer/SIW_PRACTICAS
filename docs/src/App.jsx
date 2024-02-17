import * as XLSX from 'xlsx';
import { useState } from 'react';


const proyectos = [
      {
          "nombre":"Practica 2",
          "descripcion":"Realizados todos los apartados incluidos los apartados opcionales",
          "link": "https://www.campusvirtual.uniovi.es/pluginfile.php/120787/mod_resource/content/5/2%C2%AA%20pr%C3%A1ctica%20SIW%20-%20Creaci%C3%B3n%20de%20un%20crawler%20b%C3%A1sico.pdf",
          "fechaInicio":"2024-02-15",
          "fechaFin":"2024-02-15",
          "estado":"Finalizado"
      },
      {
          "nombre":"Proyecto 3",
          "descripcion":"Ralizado el primer paso de obtener los elementos pseudo-duplicados (utilizacion de dask)",
          "link": "https://www.campusvirtual.uniovi.es/pluginfile.php/120794/mod_resource/content/7/3%C2%AA%20pr%C3%A1ctica%20SIW%20-%20Similitud%20l%C3%A9xica%20entre%20textos%20y%20detecci%C3%B3n%20de%20documentos%20cuasi-duplicados.docx.pdf",
          "fechaInicio":"2024-02-17",
          "fechaFin":"",
          "estado":"Activo"
      },
      {
          "nombre":"Proyecto 4",
          "descripcion":"Descripcion del proyecto 4",
          "link": "",
          "fechaInicio":"",
          "fechaFin":"",
          "estado":"No Activo"
      },
      {
          "nombre":"Proyecto 5",
          "descripcion":"Descripcion del proyecto 5",
          "link": "",
          "fechaInicio":"",
          "fechaFin":"",
          "estado":"No Activo"
      },
      {
          "nombre":"Proyecto 6",
          "descripcion":"Descripcion del proyecto 6",
          "link": "",
          "fechaInicio":"",
          "fechaFin":"",
          "estado":"No Activo"
      },
      {
          "nombre":"Proyecto 8",
          "descripcion":"Descripcion del proyecto 8",
          "link": "",
          "fechaInicio":"",
          "fechaFin":"",
          "estado":"No Activo"
      }
  ]



const App = () => {
  const [excelData, setExcelData] = useState(null);

  const exportToExcel = () => {
    const wb = XLSX.utils.book_new();
    const ws = XLSX.utils.json_to_sheet(proyectos);
    XLSX.utils.book_append_sheet(wb, ws, 'Proyectos');
    XLSX.writeFile(wb, 'proyectos.xlsx');
  };

  return (
   <div className="flex flex-col items-center p-16">
      <button
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-4"
        onClick={exportToExcel}
      >
        Exportar a Excel
      </button>
      
      <div className="overflow-x-auto">
        <table className="min-w-full border">
          <thead>
            <tr>
              <th className="px-4 py-2 border">Proyecto</th>
              <th className="px-4 py-2 border">Fecha Inicio</th>
              <th className="px-4 py-2 border">Status</th>
              <th className="px-4 py-2 border">Link</th>
              <th className="px-4 py-2 border">Comentarios</th>
              <th className="px-4 py-2 border">Fecha Fin</th>
            </tr>
          </thead>
          <tbody>
            {proyectos.map((proyecto, index) => (
              <tr key={index}>
                <td className="border px-4 py-2" style={{ whiteSpace: 'nowrap' }}>{proyecto.nombre}</td>
                <td className="border px-4 py-2" style={{ whiteSpace: 'nowrap' }}>{proyecto.fechaInicio}</td>
                <td className={`border px-4 py-2 ${proyecto.estado === 'Finalizado' ? 'bg-green-500' : proyecto.estado === 'Activo' ? 'bg-yellow-500' : 'bg-red-500'}`} style={{ whiteSpace: 'nowrap' }}>{proyecto.estado}</td>
                <td className="border px-4 py-2" style={{ whiteSpace: 'nowrap' }}>
                  <a href={proyecto.link}>PDF</a></td>
                <td className="border px-4 py-2" >{proyecto.descripcion}</td>
                <td className="border px-4 py-2" style={{ whiteSpace: 'nowrap' }}>{proyecto.fechaFin}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default App;
